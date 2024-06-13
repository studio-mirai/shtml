module shtml::elements {

    use std::option::{Self};
    use std::string::{Self, String};

    use sui::table_vec::{Self, TableVec};

    public struct A has key, store {
        id: UID,
        content: String,
        download: bool,
        href: String,
        rel: Option<String>,
        title: Option<String>,
        _type: Option<String>,
    }

    public struct Div<phantom T: key + store> has key, store {
        id: UID,
        children: TableVec<T>,
    }

    public struct H1 has key, store {
        id: UID,
        content: String,
    }

    public struct H2 has key, store {
        id: UID,
        content: String,
    }

    public struct H3 has key, store {
        id: UID,
        content: String,
    }

    public struct H4 has key, store {
        id: UID,
        content: String,
    }

    public struct H5 has key, store {
        id: UID,
        content: String,
    }

    public struct H6 has key, store {
        id: UID,
        content: String,
    }

    public struct Img has key, store {
        id: UID,
        alt: Option<String>,
        crossorigin: Option<String>, // anonymous or use-credentials
        decoding: Option<String>, // async or sync
        height: Option<u64>,
        ismap: bool,
        loading: Option<String>, // auto, eager, or lazy
        referrerpolicy: Option<String>, // no-referrer, no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, or unsafe-url
        sizes: vector<ImgSizesElement>,
        src: String,
        srcset: vector<ImgSrcsetElement>,
        title: Option<String>,
        usemap: Option<String>,
        width: Option<u64>,
    }

    public struct ImgSrcsetElement has store {
        src: String,
        width: u64,
    }

    public struct ImgSizesElement has store {
        condition: Option<String>,
        size: u64,
    }

    public struct Li has key, store {
        id: UID,
        content: String, 
    }

    public struct Ol has key, store {
        id: UID,
        children: TableVec<Li>,
    }

    public struct P has key, store {
        id: UID,
        content: String, 
    }

    public struct Ul has key, store {
        id: UID,
        children: TableVec<Li>,
    }

    public struct Span has key, store {
        id: UID,
        content: String,
    }

    public fun create_a(
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

    public fun create_p(
        content: String,
        ctx: &mut TxContext,
    ): P {
        let p = P {
            id: object::new(ctx),
            content: content,
        };

        p
    }
    

}