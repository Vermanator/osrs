const { hiscores } = require('osrs-json-api');



const fs = require('fs')
hiscores.getPlayer('cbk diddldum').then(function(results) {
    fs.writeFile('/Users/plaid/Documents/osrs/cbk diddldum.json', JSON.stringify(results), err => {
        if (err) {
            console.error(err)
            return
        }
          //file written successfully
          console.log("diddldum success")

    })
})
.catch(console.error);
hiscores.getPlayer('cbk kcaps').then(function(results) {
    fs.writeFile('/Users/plaid/Documents/osrs/cbk kcaps.json', JSON.stringify(results), err => {
        if (err) {
            console.error(err)
            return
        }
          //file written successfully
          console.log("kcaps success")

    })
})
.catch(console.error);
hiscores.getPlayer('cbk zip').then(function(results) {
    fs.writeFile('/Users/plaid/Documents/osrs/cbk zip.json', JSON.stringify(results), err => {
        if (err) {
            console.error(err)
            return
        }
          //file written successfully
          console.log("zip success")

    })
})
.catch(console.error);
    
