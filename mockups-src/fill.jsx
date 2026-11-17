#target photoshop
// Lit $M/job.json : {psd, out, outW, items:[{layer:"Middle Banner/Change This", html:"..."}]}
app.displayDialogs = DialogModes.NO;
var M = "/Users/jaydogo/jaydogo-portfolio/mockups-src/";
var jf = new File(M + "job.json"); jf.encoding = "UTF-8"; jf.open("r"); var job = eval("(" + jf.read() + ")"); jf.close();
var log = [];
function find(c, parts){ for (var i=0;i<c.layers.length;i++){ var l=c.layers[i]; if(l.name==parts[0]){ if(parts.length==1) return l; if(l.typename=="LayerSet") return find(l, parts.slice(1)); } } return null; }
var doc = app.open(new File(job.psd));
for (var k=0;k<job.items.length;k++){
  var it = job.items[k]; var lay = find(doc, it.layer.split("/"));
  if(!lay){ log.push("missing "+it.layer); continue; }
  doc.activeLayer = lay; executeAction(stringIDToTypeID("placedLayerEditContents"), new ActionDescriptor(), DialogModes.NO);
  var so = app.activeDocument; var w = so.width.as("px"), h = so.height.as("px");
  var png = it.png ? M + it.png : M + "art/" + it.name + ".png";
  var r = it.png ? 0 : app.system("/opt/homebrew/bin/node " + M + "render.mjs '" + M + "art/" + it.html + "' " + w + " " + h + " '" + png + "' " + (it.scale||2) + " > " + M + "art/last.log 2>&1");
  var d = new ActionDescriptor(); d.putPath(charIDToTypeID("null"), new File(png)); d.putEnumerated(charIDToTypeID("FTcs"), charIDToTypeID("QCSt"), charIDToTypeID("Qcsa"));
  executeAction(charIDToTypeID("Plc "), d, DialogModes.NO);
  var pl = so.activeLayer; pl.move(so, ElementPlacement.PLACEATBEGINNING); var b = pl.bounds; var pw = b[2].as("px")-b[0].as("px"), ph = b[3].as("px")-b[1].as("px");
  var sc = Math.max(w/pw, h/ph)*100; pl.resize(sc, sc, AnchorPosition.MIDDLECENTER);
  b = pl.bounds; pl.translate(w/2-(b[0].as("px")+b[2].as("px"))/2, h/2-(b[1].as("px")+b[3].as("px"))/2);
  so.save(); so.close(SaveOptions.DONOTSAVECHANGES); app.activeDocument = doc;
  log.push(it.layer + " " + w + "x" + h + " sys=" + r);
}
var o = new JPEGSaveOptions(); o.quality = 10;
doc.flatten(); doc.resizeImage(UnitValue(job.outW || 2610, "px"), null, 72, ResampleMethod.BICUBICSHARPER);
doc.saveAs(new File(job.out), o, true); doc.close(SaveOptions.DONOTSAVECHANGES);
log.join("\n");
