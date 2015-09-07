fs = require('fs')

execSync = require('child_process').execSync
        
uuencode = (fn) ->
        x = execSync("uuencode -m #{fn} #{fn}").toString()
        y = x.split('\n')[1..-3]
        return y.join('\n')

html_inline = (fn) ->
        comment = "#{fn} base64 encoding"
        "<!--\n#{comment}\n-->\n<img src=\"data:image/jpeg;base64,\n" +
        uuencode(fn) + '\n">'
        
        
exports.uuencode = uuencode

exports.html_inline = html_inline

if not module.parent
        fn = "godzilla-200.jpg"
        img_html = html_inline(fn)
        fs.writeFileSync("godzilla-200.html", img_html)
        
