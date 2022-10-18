#!/usr/bin/node
const fs = require("fs");

if (process.argv.length > 3) {
	fs.writeFileSync(process.argv[2], process.argv[3], (err) => {
		if (err) console.log(err);
	});
}
