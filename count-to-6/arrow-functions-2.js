const foot = {
    kick() {
        this.yelp = 'Ouch!';

        setImmediate(() => {
            console.log(this.yelp);
        });
    },
};

foot.kick();
