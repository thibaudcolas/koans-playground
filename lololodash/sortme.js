import _ from 'lodash';

export default function(collection) {
    return _.sortBy(collection, 'quantity').reverse();
};
