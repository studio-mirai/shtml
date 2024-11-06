// An element used to wrap plain text.

module shtml::text;

use std::string::{String};

public struct Text has key, store {
    id: UID,
    content: String,
}