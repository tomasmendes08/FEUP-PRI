const SolrNode = require("solr-node");
const express = require("express");


var client = new SolrNode({
    host: "127.0.0.1",
    port: "8983",
    core: "movies",
    protocol: "http"
})


const router = express.Router();

router.get("/movie", function(req, res) {
    const title = req.query["title"];
    const year = req.query["year"];

    //console.log(title,year)

    let searchQ = `original_title:"${title}"`
    searchQ += " AND original_release_date:" + year
    searchQ.replace(" ", "%20")
    const q = client.query().q(searchQ).addParams({
        wt:"json",
        indent: true,
        // rows: 10
    })
   
    client.search(q, function(err, result) {
        if (err) {
            console.log(err)
            return
        }
        const response = result.response

        response.docs[0]["original_release_date"] = response.docs[0]["original_release_date"].slice(0,10)
        response.docs[0]["streaming_release_date"] = response.docs[0]["streaming_release_date"].slice(0,10)
        response.docs[0]["genres"] = response.docs[0]["genres"].split(",")
        response.docs[0]["directors"] = response.docs[0]["directors"].split(",")
        response.docs[0]["writer"] = response.docs[0]["writer"].split(",")
        response.docs[0]["actors"] = response.docs[0]["actors"].split(",")
        response.docs[0]["production_company"] = response.docs[0]["production_company"].split(",")
        response.docs[0]["language"] = response.docs[0]["language"].split(",")
        response.docs[0]["country"] = response.docs[0]["country"].split(",")
        // for(let i = 0; i < response.docs[0].genres; i++){
        //     let aux = "";
        // }
        movie = response.docs[0]
        //console.log(movie)
        res.render("more_info", {movie: movie})
    })

    // res.render()
})

router.get("/", function(req, res) {
    console.log("Basic web page")
    res.render("index");
})

router.get("/search", (req,res) => {
    // console.log(req)
    const search = req.query["query"]
    // console.log(search)
    const searchQuery = client.query()
    .qop("OR")
    .q(search)
    .addParams({
        wt:"json",
        indent: true,
        // rows: 10
    }).dismax()
    .mltQuery("qf=" + ["original_title%5E10","movie_info%5E20","review_content%5E10"].join("%20"))

    client.search(searchQuery, function(err, result){
        if (err) {
            console.log(err)
            return
        }
        const response = result.response

        for (let i = 0; i < response.docs.length; i++) {
            response.docs[i]["original_release_date"] = response.docs[i]["original_release_date"].slice(0,10)
        }

        res.render("index", {data: {
            userQuery: search,
            movies: response.docs
            }
        })
    })

})


module.exports = router
