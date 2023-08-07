function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();

  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();

  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }

  return result;
}

function parseFileName(filename){
  if (!filename.includes(".pdf")) return filename

  filename = filename.replace(/^\d{4}_/, "").replace(".pdf", "")

  filename = filename.replace("_qp"," Question Paper").replace("_er"," Examiner Report").replace("_gt"," Grade thresholds").replace("_ms"," Mark Scheme")

  return filename
}

function getClassName(filename){
  if (!filename.includes(".pdf")) return filename

  if (filename.includes("qp")) return "qp"
  if (filename.includes("er")) return "er"
  if (filename.includes("gt")) return "gt"
  if (filename.includes("ms")) return "ms"

  return ""
}

data = JSON.parse(loadFile("fileData.json"))["DATA"]
path = "/DATA"

function updateDisplay(id) {

  data = data[id]
  path += "/" + id

  if(data == null){ // File
    window.location.href += path
  }// Next Layer

  datakeys = Object.keys(data)
  htmlcontent = `<button onclick="window.location.reload()">Back</button>`

  for(var i=0;i<datakeys.length;i++){
    htmlcontent += `<button class="`+getClassName(datakeys[i])+`" onclick="updateDisplay('`+datakeys[i]+`')">`+parseFileName(datakeys[i])+`</button>`
  } 

  document.querySelector("#main").innerHTML = htmlcontent
}
