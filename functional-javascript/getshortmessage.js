function getShortMessages(messages) {

    // Filter the messages, then map on what's left.
    return messages.filter(function(m) {
        return m.message.length < 50;
    }).map(function(m) {
        return m.message;
    });
}

module.exports = getShortMessages;
