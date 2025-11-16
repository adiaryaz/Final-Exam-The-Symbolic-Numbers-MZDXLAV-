# Final Exam The Symbolic Numbers (MZDXLAV)

Final Exam - A program to convert standard integers into a special symbolic representation based on a custom set of rules.

## 📝 Description

This program translates an integer between 1 and 3999 into a unique string of characters. The conversion logic is similar to Roman numerals, where specific letters and letter combinations represent different values. The program breaks down the input number by repeatedly subtracting the largest possible unit value until the number becomes zero.

-----

## 🎯 Problem Statement

### Input:

  * A single integer (n).

### Output:

  * A string of symbolic alphabets if $n$ is a positive integer between 1 and 3999.
  * "No Proceed" if $n$ is zero, a negative number, or greater than 3999.

### Rules:

1.  The input number **$n$** must be a positive integer within the range of **1 to 3999** for the conversion to proceed.
2.  If the input is outside this range, the program should not perform the conversion and instead output the message "No Proceed".
3.  The conversion is based on the following units:

| Symbol | Value |
| :--- | :---: |
| M | 1000 |
| ZM | 900 |
| D | 500 |
| ZD | 400 |
| Z | 100 |
| XZ | 90 |
| L | 50 |
| XL | 40 |
| X | 10 |
| AX | 9 |
| V | 5 |
| AV | 4 |
| A | 1 |

-----

## 💡 Examples

### Example 1 (n = 897)

**Input:**

```
897
```

**Output:**

```
DZZZXZVAA
```

**Explanation:** The number is broken down into **500 (D)** + **100 (Z) \* 3** + **90 (XZ)** + **5 (V)** + **1 (A) \* 2**.

### Example 2 (n = 1450)

**Input:**

```
1450
```

**Output:**

```
MZDL
```

**Explanation:** The number is broken down into **1000 (M)** + **400 (ZD)** + **50 (L)**.

### Example 3 (n = -90)

**Input:**

```
-90
```

**Output:**

```
No Proceed
```

**Explanation:** The input is a negative number, which is outside the valid range.

### Example 4 (n = 5000)

**Input:**

```
5000
```

**Output:**

```
No Proceed
```

**Explanation:** The input is greater than 3999, which is outside the valid range.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/symbolic-numbers-mzdxlav.git
    cd symbolic-numbers-mzdxlav
    ```

2.  **Run the program** (assuming the file is `MZDXLAV_UAS-H4.py`):

    ```bash
    python MZDXLAV_UAS-H4.py
    ```

    Enter a positive integer between 1 and 3999 when prompted to see the result.

-----
