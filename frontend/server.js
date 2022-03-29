/* eslint @typescript-eslint/no-var-requires: "off" */
const express = require("express");
const jwt = require("jsonwebtoken");
const cors = require("cors");
const bodyParser = require("body-parser");
const fs = require("fs");

const content = require("./sampledata/content.json");

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.json({
    message: "Welcome to the API.",
  });
});

app.get("/content", verifyToken, (req, res) => {
  jwt.verify(req.token, "the_secret_key", (err) => {
    if (err) {
      res.sendStatus(401).json({ error: "Error message" });
    } else {
      res.json({
        content,
      });
    }
  });
});

app.post("/register", (req, res) => {
  if (req.body) {
    const user = {
      name: req.body.name,
      email: req.body.email,
      password: req.body.password,
      userType: "User",
      // In a production app, you'll want to encrypt the password
    };

    const data = JSON.stringify(user, null, 2);
    var dbUserEmail = require("./sampledata/user.json").email;

    if (dbUserEmail === req.body.email) {
      res.sendStatus(400);
    } else {
      fs.writeFile("./sampledata/user.json", data, (err) => {
        if (err) {
          console.log(err + data);
        } else {
          const token = jwt.sign({ user }, "the_secret_key");
          // In a production app, you'll want the secret key to be an environment variable
          res.json({
            token,
            email: user.email,
            name: user.name,
            userType: user.UserType,
          });
        }
      });
    }
  } else {
    res.sendStatus(400).json({ error: "Error message" });
  }
});

app.post("/login", (req, res) => {
  const userDB = fs.readFileSync("./sampledata/user.json");
  const userInfo = JSON.parse(userDB);
  if (
    req.body &&
    req.body.email === userInfo.email &&
    req.body.password === userInfo.password
  ) {
    const token = jwt.sign({ userInfo }, "the_secret_key");
    // In a production app, you'll want the secret key to be an environment variable
    res.json({
      token,
      email: userInfo.email,
      name: userInfo.name,
      userType: userInfo.name,
    });
  } else {
    res.sendStatus(400).json({ error: "Error message" });
  }
});

// MIDDLEWARE
function verifyToken(req, res, next) {
  const bearerHeader = req.headers["authorization"];

  if (typeof bearerHeader !== "undefined") {
    const bearer = bearerHeader.split(" ");
    const bearerToken = bearer[1];
    req.token = bearerToken;
    next();
  } else {
    res.sendStatus(401).json({ error: "Error message" });
  }
}

app.listen(3000, () => {
  console.log("Server started on port 3000");
});
