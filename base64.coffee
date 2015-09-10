#!/usr/bin/env coffee

fs = require('fs')
path = require('path')
execSync = require('child_process').execSync

class Image

   constructor: (@src_path) ->
      this[k] = v for k,v of path.parse(@src_path)
      @data_uri_pth = @dir + '/' + @name + '_data_uri.html'
      @base64_pth = @dir + '/' + @name + '_base64.txt'

   uuencode: =>
      # make a call to external program uuencode and return result
      #
      # TODO:
      # on linux uuencode is part of the shartools package
      # and is not installed by default in ubuntu 14.04
      # 
      _ = execSync("uuencode -m #{@src_path} #{@base}").toString()
      return _

   html_inline: =>
      uu = @uuencode() 
      # lose the first line and the last two
      base64 = uu.split('\n')[1..-3].join('\n')
      comment = "<!--\n#{@base} base64 encoding\n-->"
      data_uri_pre = "data:image/jpeg;base64,\n"
      html = "#{comment}\n<img src=\"#{data_uri_pre}#{base64}\n\">\n"
      return html

class Images

   constructor: (@paths) ->
      @images = (new Image(pth) for pth in @paths)

   write_html: =>
      for img in @images
         console.log 'writing: ' + img.data_uri_pth
         fs.writeFileSync(img.data_uri_pth, img.html_inline())
      
if not module.parent
   images = new Images(process.argv[2..])
   images.write_html()

exports.Image = Image
