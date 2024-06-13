module shtml::h6 {

    use std::string::{String};

    public struct H6 has key, store {
        id: UID,
        content: String,
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): H6 {
        let h6 = H6 {
            id: object::new(ctx),
            content: content,
        };

        h6
    }
}