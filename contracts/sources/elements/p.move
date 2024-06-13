module shtml::p {

    use std::string::{String};

    public struct P has key, store {
        id: UID,
        content: String, 
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): P {
        let p = P {
            id: object::new(ctx),
            content: content,
        };

        p
    }
}