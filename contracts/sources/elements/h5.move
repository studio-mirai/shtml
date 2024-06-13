module shtml::h5 {

    use std::string::{String};

    public struct H5 has key, store {
        id: UID,
        content: String,
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): H5 {
        let h5 = H5 {
            id: object::new(ctx),
            content: content,
        };

        h5
    }
}