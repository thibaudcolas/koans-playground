import _ from 'lodash';

export default function(collection) {
    return _.where(collection, { active: true});
};
