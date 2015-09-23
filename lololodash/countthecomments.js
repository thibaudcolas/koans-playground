import _ from 'lodash'

export default function(collection) {
    return _.chain(collection)
            .groupBy('username')
            .map((comments, username) => {
                return {
                    username: username,
                    comment_count: _.size(comments),
                }
            })
            .sortBy('comment_count')
            .reverse()
}
