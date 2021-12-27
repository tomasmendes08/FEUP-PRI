const SolrNode = require("solr-node");
const express = require("express");

var client = new SolrNode({
    host: "127.0.0.1",
    port: "8983",
    core: "movies",
    protocol: "http"
})


const router = express.Router();

// router.post("/movie", function(req, res) {
//     console.log(req.body)
//     let link = req.params
//     const searchQ = "imdb_title_id:" + link
//     const q = client.query().q(searchQ).addParams({
//         wt:"json",
//         indent: true,
//         // rows: 10
//     })
   
//     client.search(q, function(err, result) {
//         if (err) {
//             console.log(err)
//             return
//         }
//         const response = result.response
//         console.log(response)
//     })

//     // res.render()
// })

router.get("/", function(req, res) {
    console.log("Basic web page")
    res.render("index");
})

router.get("/search", (req,res) => {
    const search = req.query["query"];

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

        // console.log(response);
        // console.log(response.docs[0]["original_release_date"]);

        for (let i = 0; i < response.docs.length; i++) {
            response.docs[i]["original_release_date"] = response.docs[i]["original_release_date"].slice(0,10);
        }

        res.render("index", {data: {
            userQuery: search,
            movies: response.docs
            }
        })
    })

})


module.exports = router
