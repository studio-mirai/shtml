module shtml::img {

    use std::option::{Self};
    use std::string::{Self, String, utf8};

    use sui::table_vec::{Self, TableVec};

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

    const EInvalidLoadingAttrValue: u64 = 1;
    const EInvalidCrossoriginPolicyAttrValue: u64 = 2;
    const EInvalidDecodingAttrValue: u64 = 3;
    const EInvalidReferrerPolicyAttrValue: u64 = 3;

    public fun create(
        alt: Option<String>,
        crossorigin: Option<String>,
        decoding: Option<String>,
        height: Option<u64>,
        ismap: bool,
        loading: Option<String>,
        referrerpolicy: Option<String>,
        src: String,
        title: Option<String>,
        usemap: Option<String>,
        width: Option<u64>,
        ctx: &mut TxContext,
    ): Img {
        // Validate `crossorigin` attribute value.
        if (crossorigin.is_some()) {
            let v = vector<String>[
                utf8(b"anonymous"),
                utf8(b"use-credentials"),
            ];
            assert!(v.contains(crossorigin.borrow()), EInvalidCrossoriginPolicyAttrValue);
        };

        // Validate `decoding` attribute value.
        if (decoding.is_some()) {
            let v = vector<String>[
                utf8(b"async"),
                utf8(b"sync"),
            ];
            assert!(v.contains(decoding.borrow()), EInvalidDecodingAttrValue);
        };

        // Validate `loading` attribute value.
        if (loading.is_some()) {
            let v = vector<String>[
                utf8(b"auto"),
                utf8(b"eager"),
                utf8(b"lazy"),
            ];
            assert!(v.contains(loading.borrow()), EInvalidLoadingAttrValue);
        };

        // Validate `referrerpolicy` attribute value.
        if (referrerpolicy.is_some()) {
            let v = vector<String>[
                utf8(b"no-referrer"),
                utf8(b"no-referrer-when-downgrade"),
                utf8(b"origin"),
                utf8(b"origin-when-cross-origin"),
                utf8(b"same-origin"),
                utf8(b"strict-origin"),
                utf8(b"strict-origin-when-cross-origin"),
                utf8(b"unsafe-url"),
            ];
            assert!(v.contains(referrerpolicy.borrow()), EInvalidReferrerPolicyAttrValue);
        };

        let img = Img {
            id: object::new(ctx),
            alt: alt,
            crossorigin: crossorigin,
            decoding: decoding,
            height: height,
            ismap: ismap,
            loading: loading,
            referrerpolicy: referrerpolicy,
            sizes: vector::empty(),
            src: src,
            srcset: vector::empty(),
            title: title,
            usemap: usemap,
            width: width,
        };

        img
    }

}



