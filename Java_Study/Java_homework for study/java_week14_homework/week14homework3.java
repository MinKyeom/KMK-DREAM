package school_4_2_1;

import java.util.*;

class week14homework3 {
	public static void main(String args[]) {
		TreeMap<Integer,String> tm = new TreeMap<Integer,String>();
		tm.put(88,"국어");
		tm.put(100,"영어");
		tm.put(76,"수학");
		tm.put(80,"사회");
		tm.put(69,"과학");
		
		Map.Entry<Integer,String> me = tm.firstEntry();
		System.out.println("가장 낮은 성적은 " + me.getKey() + "점이며 과목은 "+ me.getValue() + "입니다");
		me = tm.lastEntry();
		System.out.println("가장 높은 성적은 " + me.getKey() + "점이며 과목은 "+ me.getValue() + "입니다");
		Map<Integer,String> cd = tm.headMap(80);
		System.out.println("학점 C,D에 해당하는 과목과 점수 : " + cd);
		Map<Integer,String> ab = tm.tailMap(80);
		System.out.println("학점 A,B에 해당하는 과목과 점수 : " + ab);
		System.out.println("점수 순으로 출력(낮은 점수 부터) : " + tm);
		System.out.println("점수 순으로 출력(높은 점수 부터) : " + tm.descendingMap());
	}
}