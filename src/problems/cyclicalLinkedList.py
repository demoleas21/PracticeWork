def containsCycle(firstNode):
    nextNodeSlow = firstNode.next
    nextNodeFast = firstNode.next.next
    while nextNodeFast.next.next:
        if nextNodeSlow == nextNodeFast:
            return True
        nextNodeSlow = nextNodeSlow.next
        nextNodeFast = nextNodeFast.next.next
    return False


def main():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')
    d = LinkedListNode('D')

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    print containsCycle(a)
