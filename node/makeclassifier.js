var bayes = require('bayes')
var fs = require('fs')

var classifier = bayes()

var dir = "cats/";
var files = fs.readdirSync(dir);
var target = 100000;
files.forEach(function(file) {
  var data = fs.readFileSync(dir+file, 'utf8');
  var lines = data.split("\n");
  var count = 0;
  while(count < target){
    for(var i = 0; i< lines.length; i++){
      classifier.learn(lines[i].toLowerCase(), file);
      var parts = lines[i].toLowerCase().split(" ");
      for(var j = 0; j<parts.length;j++){
        parts[j]=parts[j]+"s";
      }
      classifier.learn(parts.join(" "), file)
    }
    count += lines.length * 2;
    for(var i = 0;i<10;i++){
      classifier.learn(file, file)
    }
    count += 10;
  }
});

// serialize the classifier's state as a JSON string.
var stateJson = classifier.toJson()
fs.writeFile("bayes.json", stateJson);
