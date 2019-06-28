import Control.Monad
import Data.Char

main = do
    nTests <- readLn
    forM [1..nTests] $ \i -> do
        n <- getLine
        let (l, r) = solve n
        putStrLn $ "Case #" ++ (show i) ++ ": " ++ l ++ " " ++ r

separate d
    | d == 4 = (2, 2)
    | otherwise = (0, d)

solve' ns = do
    let pairs = map separate ns
    unzip pairs

digitsToStr ns = do
    let ns' = dropWhile (== 0) ns :: [Int]
    concat $ map show ns'

solve n = do
    let ns = map digitToInt n
        (l, r) = solve' ns
    (digitsToStr l, digitsToStr r)
