module shtml::body {

    use std::string::{String};

    public struct A has key, store {
        id: UID,
        content: String,
        download: bool,
        href: String,
        rel: Option<String>,
        title: Option<String>,
        _type: Option<String>,
    }

    public struct Body has key, store {
        id: UID,
        children: vector<ID>,
    }

    public fun create(
        ctx: &mut TxContext,
    ): Body {
        let body = Body {
            id: object::new(ctx),
            children: vector::empty(),
        };

        body
    }

    public fun add_child<T: key + store>(
        body: &mut Body,
        child: T,
        index: u64,
    ) {
        body.children.insert(object::id(&child), index);
        transfer::public_transfer(child, object::uid_to_address(&body.id));
    }

    public fun swap_child(
        body: &mut Body,
        child1: u64,
        child2: u64
    ) {
        body.children.swap(child1, child2);
    }
}