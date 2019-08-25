import qualified Control.Monad as Monad
import qualified Data.Set      as Set

data Sign = Sign { index :: Int
                 , m     :: Int
                 , n     :: Int
                 } deriving (Show)

reverseSign (Sign index m n) = Sign index n m

spanContiguousSigns signs = let headM = m $ head signs
                                (signsSameAsHeadM, restSigns) = span ((== headM) . m) signs
                                headN = n $ head restSigns
                                isContiguous sign = m sign == headM || n sign == headN
                                contiguousSigns = signsSameAsHeadM ++ takeWhile isContiguous restSigns
                             in (contiguousSigns, restSigns)

toRange contiguousSigns = (index $ head contiguousSigns, index $ last contiguousSigns)

signsToContiguousRanges signs = let (contiguousSigns, restSigns) = spanContiguousSigns signs
                                    range = toRange contiguousSigns
                                 in if null restSigns then [range]
                                                      else range : signsToContiguousRanges restSigns

lineToSign index line = let [d, a, b] = words line
                         in Sign index (read d + read a) (read d - read b)

size (start, end) = end - start + 1

main = do
  nTests <- read <$> getLine
  Monad.forM_ [1..nTests] $ \i -> do
    nSigns <- read <$> getLine
    signLines <- Monad.replicateM nSigns getLine
    let signs = zipWith lineToSign [0..] signLines
        contiguousRanges = signsToContiguousRanges signs ++ signsToContiguousRanges (map reverseSign signs)
        maxSize = maximum $ map size contiguousRanges
        count = Set.size $ Set.fromList $ filter ((== maxSize) . size) contiguousRanges
    putStr $ "Case #" ++ show i ++ ": " ++ show maxSize ++ " " ++ show count ++ "\n"
