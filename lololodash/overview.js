import _ from 'lodash'

export default function(collection) {
    return _.chain(collection)
        .groupBy('article')
        .map((articles) => {
            return {
                article: articles[0].article,
                total_orders: _.chain(articles)
                    .pluck('quantity')
                    .reduce((sum, num) => sum + num, 0)
                    .value()
            }
        })
        .value()
        .reverse()
}
