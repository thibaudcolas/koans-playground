import _ from 'lodash'

export default function(collection) {
    const sum = _.pluck(collection, 'income')
        .reduce((sum, num) => sum + num, 0)
    const average = sum / collection.length

    return {
        average: average,
        underperform: _.chain(collection)
            .filter(item => item.income <= average)
            .sortBy('income')
            .value(),
        overperform: _.chain(collection)
            .filter(item => item.income > average)
            .sortBy('income')
            .value(),
    }
}
