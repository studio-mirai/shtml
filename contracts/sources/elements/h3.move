module shtml::h3 {

    use std::string::{String};

    public struct H3 has key, store {
        id: UID,
        content: String,
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): H3 {
        let h3 = H3 {
            id: object::new(ctx),
            content: content,
        };

        h3
    }
}