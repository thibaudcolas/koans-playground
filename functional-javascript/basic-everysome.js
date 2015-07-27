function checkUsersValid(goodUsers) {

    return function allUsersValid(submittedUsers) {

        // For every submittedUser, check that it is also in the goodUsers.
        return submittedUsers.every(function(subUser) {
            return goodUsers.some(function(goodUser) {
                return goodUser.id === subUser.id;
            });
        });
    };
}

module.exports = checkUsersValid;
