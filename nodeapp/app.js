var express = require("express");
const path = require("path")
const routes = require("./routes");

var app = express()

app.set("port", 3000)
app.set("views", path.join(__dirname, "views"))
app.set("view engine", "ejs")
app.engine('ejs', require('ejs').__express);
app.use(routes)

app.listen(3000, function() {
    console.log("Server started on port 3000")
})




