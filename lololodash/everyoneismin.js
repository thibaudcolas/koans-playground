import _ from 'lodash'

export default function(collection) {
    const groups = {
        hot: [],
        warm: [],
    }

    _.forEach(collection, (temperatures, name) => {
        if (_.every(temperatures, t => t > 19)) {
            groups.hot.push(name)
        } else if (_.some(temperatures, t => t > 19)) {
            groups.warm.push(name)
        }
    })

    return groups
}
