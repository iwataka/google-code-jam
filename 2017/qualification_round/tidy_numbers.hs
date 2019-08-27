import Control.Monad
import Data.Char

main = do
    nTests <- readLn
    forM [1..nTests] $ \i -> do
        num <- getLine
        let ans = solve num
        putStrLn $ "Case #" ++ (show i) ++ ": " ++ ans

toDigits :: [Char] -> [Int]
toDigits = map digitToInt

toStr digits = do
    let dss = map show digits
    foldl (++) "" dss

minusDigit digits i
    | i <= 0 = digits
    | l > r = front ++ [l - 1] ++ (replicate (length rear + 1) 9)
    | otherwise = digits
    where
        (front, rear') = splitAt (i - 1) digits
        l:r:rear = rear'

removeLeadingZero digits
    | length digits == 0 = digits
    | h == 0 = removeLeadingZero ds
    | otherwise = digits
    where h:ds = digits

solve' digits = do
    let end = length digits - 1
    foldl minusDigit digits [end,end-1..1]

solve num = do
    let digits = toDigits num
    let ans = removeLeadingZero $ solve' digits
    if length ans == 0
        then "0"
        else toStr ans
