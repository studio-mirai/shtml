module shtml::li {

    use std::string::{String};

    public struct Li has key, store {
        id: UID,
        content: String, 
    }

    public fun create(
        content: String,
        ctx: &mut TxContext,
    ): Li {
        let li = Li {
            id: object::new(ctx),
            content: content,
        };

        li
    }

    public(package) fun id(
        li: &Li,
    ): ID {
        object::id(li)
    }
}