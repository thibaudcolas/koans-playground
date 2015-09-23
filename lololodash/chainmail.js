import _ from 'lodash'

export default function(collection) {
    return _.chain(collection)
        .map(item => `${item}Chained`)
        .map(item => item.toUpperCase())
        .sortBy()
        .value()
}
