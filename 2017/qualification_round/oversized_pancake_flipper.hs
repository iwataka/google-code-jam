import           Control.Monad

data Pancake = Happy | Blank deriving (Eq, Show)

main = do
    nTests <- readLn
    forM [1..nTests] $ \i -> do
        a <- getLine
        let [pancakesChars, flipperSize'] = words a
            flipperSize = read flipperSize' :: Int
            pancakes = map toPancake pancakesChars
            (canFlipAll, flipCount) = solve flipperSize pancakes
            answer = if canFlipAll
                        then (show flipCount)
                        else "IMPOSSIBLE"
        putStrLn $ "Case #" ++ (show i) ++ ": " ++ answer

toPancake c = case c of
    '+' -> Happy
    '-' -> Blank
    _   -> error $ "Invalid character: " ++ [c]

flipOne p = case p of
    Happy -> Blank
    Blank -> Happy

flipMany :: Int -> [Pancake] -> Int -> [Pancake]
flipMany flipperSize pancakes start = do
    let (front, rear') = splitAt start pancakes
    let (mid, rear) = splitAt flipperSize rear'
    front ++ (map flipOne mid) ++ rear

flipManyIfNeeded :: Int -> [Pancake] -> Int -> ([Pancake], Bool)
flipManyIfNeeded flipperSize pancakes start = case (pancakes !! start) of
    Happy -> (pancakes, False)
    Blank -> (pancakes', True)
        where pancakes' = flipMany flipperSize pancakes start

flipManyAndCount :: Int -> [Pancake] -> Int -> Int -> ([Pancake], Int)
flipManyAndCount flipperSize pancakes start count = do
    let (ps, flipped) = flipManyIfNeeded flipperSize pancakes start
    (ps, count + (if flipped then 1 else 0))

solve :: Int -> [Pancake] -> (Bool, Int)
solve flipperSize pancakes = do
    let f = \(ps, count) start -> flipManyAndCount flipperSize ps start count
    let l = length pancakes
    let (ps, flipCount) = foldl f (pancakes, 0) [0..(l - flipperSize)]
    (all (== Happy) ps, flipCount)
