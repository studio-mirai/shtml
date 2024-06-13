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
}