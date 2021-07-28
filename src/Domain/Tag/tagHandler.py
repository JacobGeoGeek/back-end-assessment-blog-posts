from typing import List, Set

class TagHandler:
    def filter_common_tags(self, tags: str, saved_tags:List[str]) -> List[str]:
        tagItems: Set[str] = set(tags.split(","))
        return list(set(saved_tags).intersection(tagItems))

    def filter_new_tags(self, tags: str, saved_tags: List[str]) -> List[str]:
        tagItems: Set[str] = set(tags.split(","))
        return list(tagItems.difference(saved_tags))
