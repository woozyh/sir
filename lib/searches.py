#! /usr/bin/python3.11.8

class search(object):

    def intersecting(p1, p2) -> list[int, int]:
        answer = []
        while (p1.head != None and p2.head != None):
            if p1.head.docId == p2.head.docId:
                answer.append(p1.head.docId)
                p1.head = p1.head.next
                p2.head = p2.head.next
            elif p1.head.docId < p2.head.docId:
                p1.head = p1.head.next
            else:
                p2.head = p2.head.next
        return answer

