import _ from 'lodash'

export default function(data) {
    const loginCount = data.login.length
    const template = 'Hello <%= name %> (logins: <%= login.length %>)'

    return _.template(template)(data)
}
