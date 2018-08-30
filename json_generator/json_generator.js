#!/usr/bin/env node
'use strict';

var jsf = require('json-schema-faker');
var fs = require('fs');
const args = require('minimist')(process.argv.slice(2));

var schema = JSON.parse(fs.readFileSync(args.filePath));
jsf.resolve(schema).then(function(result) {
    fs.writeFile(args.outputFilePath, JSON.stringify(result, null, 2), function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });

});
