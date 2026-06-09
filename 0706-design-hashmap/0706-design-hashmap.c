#include <stdlib.h>

#define HASH_SIZE 1009

typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

typedef struct {
    Node** buckets;
    int size;
} MyHashMap;

int hash(int key, int size) {
    return key % size;
}

MyHashMap* myHashMapCreate() {
    MyHashMap* obj = (MyHashMap*)malloc(sizeof(MyHashMap));

    obj->size = HASH_SIZE;

    // Node* 타입의 포인터를 HASH_SIZE개 저장할 배열 생성
    obj->buckets = (Node**)calloc(obj->size, sizeof(Node*));

    return obj;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    int index = hash(key, obj->size);
    Node* current = obj->buckets[index];

    // 이미 존재하는 key라면 value만 갱신
    while (current != NULL) {
        if (current->key == key) {
            current->value = value;
            return;
        }
        current = current->next;
    }

    // 존재하지 않는 key라면 새 노드를 맨 앞에 삽입
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = obj->buckets[index];

    obj->buckets[index] = newNode;
}

int myHashMapGet(MyHashMap* obj, int key) {
    int index = hash(key, obj->size);
    Node* current = obj->buckets[index];

    while (current != NULL) {
        if (current->key == key) {
            return current->value;
        }
        current = current->next;
    }

    return -1;
}

void myHashMapRemove(MyHashMap* obj, int key) {
    int index = hash(key, obj->size);
    Node* current = obj->buckets[index];
    Node* prev = NULL;

    while (current != NULL) {
        if (current->key == key) {
            // 삭제할 노드가 첫 번째 노드인 경우
            if (prev == NULL) {
                obj->buckets[index] = current->next;
            }
            // 삭제할 노드가 중간 또는 끝 노드인 경우
            else {
                prev->next = current->next;
            }

            free(current);
            return;
        }

        prev = current;
        current = current->next;
    }
}

void myHashMapFree(MyHashMap* obj) {
    for (int i = 0; i < obj->size; i++) {
        Node* current = obj->buckets[i];

        while (current != NULL) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }

    free(obj->buckets);
    free(obj);
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/