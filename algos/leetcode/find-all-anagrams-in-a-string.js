#https://leetcode.com/problems/find-all-anagrams-in-a-string/
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */

function areMapsIdentical(map1, map2) {
    // Check if the sizes are different

    //console.log(map1,map2);

    if (map1.size !== map2.size) {
        return false;
    }

    // Iterate over entries of the first map
    for (let [key, value] of map1) {
        // Check if the second map has the key and the same value
        if (!map2.has(key) || map2.get(key) !== value) {
            return false;
        }
    }

    return true;
}

var findAnagrams = function(s, p) {

    if(p.length > s.length) return []

    let output = [];

    let pMap = new Map();
    for(i=0; i<p.length; i++){
        let c = p.charAt(i);
        if(pMap.get(c)){
            pMap.set(c, pMap.get(c) + 1);
        }else{
            pMap.set(c, 1);
        }
    }

    console.log(pMap);
    
    let currentMap = new Map();

    for(i=0; i<p.length; i++){
        let c = s.charAt(i);
        if(currentMap.get(c)){
            currentMap.set(c, currentMap.get(c) + 1);
        }else{
            currentMap.set(c, 1);
        }
    }

    if(areMapsIdentical(currentMap,pMap)){
        output.push(0);
    }

    for(var i=p.length; i<s.length; i++){
        let c = s.charAt(i);
        let prevC = s.charAt(i-p.length);
        //console.log(c);
        //console.log(prevC);

        if(currentMap.get(prevC) == 1){
             currentMap.delete(prevC);
        }else{
            currentMap.set(prevC, currentMap.get(prevC) - 1);
        }
        
        if(currentMap.get(c)){
            currentMap.set(c, currentMap.get(c) + 1);
        }else{
            currentMap.set(c, 1);
        }

        if(areMapsIdentical(currentMap,pMap)){
            output.push(i-p.length+1);
        }
    }

    return output;
    
};