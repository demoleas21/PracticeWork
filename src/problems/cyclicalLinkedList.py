def containsCycle(firstNode):
    nextNodeSlow = firstNode.next
    nextNodeFast = firstNode.next.next
    while nextNodeFast.next.next:
        if nextNodeSlow == nextNodeFast:
            return True
        nextNodeSlow = nextNodeSlow.next
        nextNodeFast = nextNodeFast.next.next
    return False
