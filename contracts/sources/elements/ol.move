module shtml::ol {

    use std::string::{String};
    use std::vector::{Self};

    use shtml::li::{Self, Li};

    public struct Ol has key, store {
        id: UID,
        children: vector<ID>,
    }

    public fun create(
        ctx: &mut TxContext,
    ): Ol {
        let li = Ol {
            id: object::new(ctx),
            children: vector::empty(),
        };

        li
    }

    public fun add_child(
        li: Li,
        ol: &mut Ol,
    ) {
        ol.children.push_back(li.id());
        transfer::public_transfer(li, object::uid_to_address(&ol.id));
    }
}