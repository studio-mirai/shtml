module shtml::h1 {

    use std::string::{String};

    public struct H1 has key, store {
        id: UID,
        content: String,
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): H1 {
        let h1 = H1 {
            id: object::new(ctx),
            content: content,
        };

        h1
    }
}