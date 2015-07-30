// var loremIpsum = {
//   "name": "lorem-ipsum",
//   "version": "0.1.1",
//   "dependencies": {
//     "optimist": {
//       "version": "0.3.7",
//       "dependencies": {
//         "wordwrap": {
//           "version": "0.0.2"
//         }
//       }
//     },
//     "inflection": {
//       "version": "1.2.6"
//     }
//   }
// }

// getDependencies(loremIpsum) // => [ 'inflection@1.2.6', 'optimist@0.3.7', 'wordwrap@0.0.2' ]

function getDependencies(tree) {
    var deps = tree.dependencies || {};
    var dep;

    var result = Object.keys(deps).reduce(function(acc, key) {
        dep = deps[key];

        acc.push(key + '@' + dep.version);

        return acc.concat(getDependencies(dep)).reduce(function(a, depStr) {
            if (a.indexOf(depStr) === -1) {
                a.push(depStr);
            }

            return a;
        }, []);
    }, []);

    return result.sort();
}

module.exports = getDependencies;
