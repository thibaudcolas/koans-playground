import _ from 'lodash'

export default function(collection) {
    return _.forEach(collection, (item, key) => {
        let size

        if (item.population > 1) {
            size = 'big'
        } else if (item.population > 0.5) {
            size = 'med'
        } else {
            size = 'small'
        }

        item.size = size
    })
}
