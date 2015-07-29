function Spy(target, method) {
    var original = target[method];
    var self = this;

    self.count = 0;

    target[method] = function() {
        self.count++;
        return original.apply(this, arguments);
    };

    return self;
}

module.exports = Spy;
