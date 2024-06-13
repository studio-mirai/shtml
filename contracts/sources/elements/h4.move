module shtml::h4 {

    use std::string::{String};

    public struct H4 has key, store {
        id: UID,
        content: String,
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): H4 {
        let h4 = H4 {
            id: object::new(ctx),
            content: content,
        };

        h4
    }
}