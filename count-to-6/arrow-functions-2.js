const foot = {
    kick() {
        this.yelp = 'Ouch!';

        setImmediate(() => {
            // Since we used an arrow function, `this` here is the same as `this` outside of the function.
            console.log(this.yelp);
        });
    },
};

foot.kick();
