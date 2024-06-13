module shtml::a {

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

    public fun create(
        content: String,
        download: bool,
        href: String,
        rel: Option<String>,
        title: Option<String>,
        _type: Option<String>,
        ctx: &mut TxContext,
    ): A {
        let a = A {
            id: object::new(ctx),
            content: content,
            download: download,
            href: href,
            rel: rel,
            title: title,
            _type: _type,
        };

        a
    }
}