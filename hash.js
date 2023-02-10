class HashTable {
  constructor(size = 53) {
    this.hashMap = new Array(size);
  }
  _hash(key) {
    let total = 0;
    let prime = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let value = key[i].charCodeAt(0) - 96;
      total = (total * prime + value) % this.hashMap.length;
    }
    return total;
  }
  set(key, value) {
    let index = this._hash(key);
    if (!this.hashMap[index]) {
      this.hashMap[index] = [];
    }
    this.hashMap[index].push([key, value]);
  }
  get(key) {
    let index = this._hash(key);
    if (this.hashMap[index]) {
      for (let i = 0; i < this.hashMap[index].length; i++) {
        if (this.hashMap[index][i][0] === key) {
          return this.hashMap[index][i][1];
        }
      }
      return undefined;
    }
  }
  keys() {
    let keysArr = [];
    for (let i = 0; i < this.hashMap.length; i++) {
      if (this.hashMap[i]) {
        for (let j = 0; j < this.hashMap[i].length; j++) {
          if (!keysArr.includes(this.hashMap[i][j][0])) {
            keysArr.push(this.hashMap[i][j][0]);
          }
        }
      }
    }
    return keysArr;
  }
  values() {
    let valuesArr = [];
    for (let i = 0; i < this.hashMap.length; i++) {
      if (this.hashMap[i]) {
        for (let j = 0; j < this.hashMap[i].length; j++) {
          if (!valuesArr.includes(this.hashMap[i][j][1])) {
            valuesArr.push(this.hashMap[i][j][1]);
          }
        }
      }
    }
    return valuesArr;
  }
}
let ht = new HashTable(17);
ht.set("maroon", "#800000");
ht.set("yellow", "#FFFF00");
ht.set("olive", "#808000");
ht.set("salmon", "#FA8072");
ht.set("lightcoral", "#F08080");
ht.set("mediumvioletred", "#C71585");
ht.set("plum", "#DDA0DD");
ht.set("purple", "#DDA0DD");
ht.set("violet", "#DDA0DD");

ht.keys().forEach(function (key) {
  console.log(ht.get(key));
});
