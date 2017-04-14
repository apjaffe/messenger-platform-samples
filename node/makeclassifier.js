var bayes = require('bayes')
var fs = require('fs')

var classifier = bayes()

var dir = "cats/";
var files = fs.readdirSync(dir);
files.forEach(function(file) {
  var data = fs.readFileSync(dir+file, 'utf8');
  var lines = data.split("\n");
  for(var i = 0; i< lines.length; i++){
    classifier.learn(lines[i].toLowerCase(), file);
  }
});

// serialize the classifier's state as a JSON string.
var stateJson = classifier.toJson()
fs.writeFile("bayes.json", stateJson);
